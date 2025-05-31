# def generate_partial_bio_format_v1(json_circulars):
#     new_list = []
#     for sub_cir in json_circulars:
#         new_obj = sub_cir.copy()
#         text = sub_cir["body"]
#         new_obj["body"] = text.replace("\n", "")
#         encoding = tokenizer(
#             text,
#             return_offsets_mapping=True,
#             return_tensors="pt",
#             truncation=True,
#             return_special_tokens_mask=True
#         )
#
#         input_ids = encoding["input_ids"][0]
#         offsets = encoding["offset_mapping"][0].tolist()
#         word_ids = encoding.word_ids()
#         tokens = tokenizer.convert_ids_to_tokens(input_ids)
#
#         token_list = []
#         current_word_id = None
#         current_token = ""
#         current_start = None
#         current_end = None
#
#         for token, (start, end), word_id in zip(tokens, offsets, word_ids):
#             if word_id is None:
#                 continue  # Skip special tokens like [CLS], [SEP]
#             if word_id != current_word_id:
#                 # Save the previous token
#                 if current_token:
#                     token_list.append({
#                         "token": current_token,
#                         "position": {
#                             "start": current_start,
#                             "end": current_end},
#                         "label": "O"
#                     })
#                 # Start new token
#                 current_token = text[start:end]
#                 current_start = start
#                 current_end = end
#                 current_word_id = word_id
#             else:
#                 # Same word_id → add subword
#                 current_token += text[start:end]
#                 current_end = end
#
#         # Add the last token
#         if current_token:
#             token_list.append({
#                 "token": current_token,
#                 "position": {
#                     "start": current_start,
#                     "end": current_end},
#                 "label": "O"
#             })
#         new_obj["token_list"] = token_list
#         pipline_output_arr = []
#         for i in range(0, len(token_list), 200):
#             chunk_arr = token_list[i : i + 200]
#             chunk_text = " ".join([token["token"] for token in chunk_arr])
#             pipline_output_arr.extend(ner_pipeline(chunk_text))
#
#         new_obj["new_pipeline_output"] = pipline_output_arr
#         new_list.append(new_obj)
#     return new_list
# output_bio = generate_partial_bio_format_v1(output)
# print(output_bio[0]["body"])
# print(output_bio[0]["token_list"])
# print(output_bio[0]["new_pipeline_output"])