import json
import torch
import os

def get_circulars(sub_cirs):
    json_circulars = []
    for sub_cir in sub_cirs:
        with open('./archive.json/{}.json'.format(sub_cir), 'r') as f:
            data = json.load(f)
            json_circulars.append(data)
    return json_circulars

def merge_subwords(tokens):
    merged = []
    buffer = ""
    buffer_start = None
    buffer_end = None
    buffer_label = None

    for token_info in tokens:
        token = token_info['token']
        start = token_info['start']
        end = token_info['end']
        label = token_info['label']
        if token == '[CLS]' or token == '[SEP]':
            merged.append({
                "token": token,
                "start": start,
                "end": end,
                "label": label
            })
            continue

        if token.startswith('##'):
            # It's a subword — merge with buffer
            buffer += token[2:]
            buffer_end = end
        else:
            # Commit previous buffer if exists
            if buffer:
                merged.append({
                    "token": buffer,
                    "start": buffer_start,
                    "end": buffer_end,
                    "label": buffer_label
                })
                buffer = ""
                buffer_start = buffer_end = buffer_label = None

            # Start new buffer
            buffer = token
            buffer_start = start
            buffer_end = end
            buffer_label = label

    # Commit the final buffer
    if buffer:
        merged.append({
            "token": buffer,
            "start": buffer_start,
            "end": buffer_end,
            "label": buffer_label
        })

    return merged

def get_att(cir, nlp, tokenizer,model, label_list):
    text = cir["body"]
    doc = nlp(text)
    sentences = [sent.text.strip() for sent in doc.sents]
    # print(sentences)
    sentence_level_tokenization = []
    for sent in sentences:
        # print("sent", sent)
        sentence_results = []
        inputs = tokenizer(sent, return_tensors="pt", return_offsets_mapping=True, truncation=True)
        offset_mapping = inputs.pop("offset_mapping")
        # Move input tensors to device
        inputs = {k: v.cpu() for k, v in inputs.items()}

        with torch.no_grad():
            outputs = model(**inputs, return_dict=True)

        logits = outputs.logits.cpu()

        predictions = torch.argmax(logits, dim=2)

        tokens = tokenizer.convert_ids_to_tokens(inputs["input_ids"][0])
        offsets = offset_mapping[0].tolist()
        for token, offset, pred_id in zip(tokens, offsets, predictions[0]):
            label = label_list[pred_id.item()]
            sentence_results.append({
                "token": token,
                "start": offset[0],
                "end": offset[1],
                "label": label
            })
        sentence_level_tokenization.append({
            "sent": sent,
            "result":merge_subwords(sentence_results)})
        # Output includes all tokens — even those labeled "O"
    return sentence_level_tokenization

def generate_partial_sentence_level_bio_format(json_circulars, nlp, tokenizer,model, label_list):
    new_list = []
    for sub_cir in json_circulars:
        new_obj = sub_cir.copy()
        text = sub_cir["body"]
        new_obj["body"] = text.replace("\n", " ")
        new_obj["new_pipeline_output"] = get_att(new_obj,nlp, tokenizer,model, label_list)
        new_list.append(new_obj)
    return new_list

def write_bio(output_path, cir):
    with open(output_path, "w", encoding="utf-8") as f:
        sentence_level_tokenization = cir["new_pipeline_output"]
        for sent_obj in sentence_level_tokenization:
            sent = sent_obj["sent"]
            result = sent_obj["result"]
            f.write(f"sentence:  {sent}\n")
            for tok in result:
                word = tok["token"]
                label = tok["label"]
                f.write(f"{word} {label}\n")
        f.write("\n")

def create_bio_files(outputs, file_path_prefix):
    os.makedirs(file_path_prefix, exist_ok=True)
    for bio_output in outputs:
        # print("bio_output", bio_output)
        write_bio(f"{file_path_prefix}/{bio_output['circularId']}.txt", bio_output)