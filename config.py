# config.py

# CONFIG = [
#     {
#         "ne": False,
#         "wer_rate": 0,
#         "word_error": 1,
#         "force": False
#     },
#     {
#         "ne": True,
#         "wer_rate": 1,
#         "word_error": 15,
#         "force": True
#     }, {
#         "ne": False,
#         "wer_rate": 1,
#         "word_error": 15,
#         "force": True
#     }, {
#         "ne": "All",
#         "wer_rate": 1,
#         "word_error": 15,
#         "force": True
#     }
# ]

CONFIG = []

# # Define the parameters to iterate over
# ne_values = [True, False, "All"]
# wer_rates = [round(i * 0.1, 1) for i in range(0, 11)]  # 0.1 to 1.0 with a step of 0.1
# # wer_rates = [1]
# word_errors = [1,2,3,4,5]
#
# # Generate the configurations
# for word_error in word_errors:
#     for ne in ne_values:
#         for wer_rate in wer_rates:
#             CONFIG.append({
#                 "ne": ne,
#                 "wer_rate": wer_rate,
#                 "character_per_word_error": word_error,
#                 "force": True
#             })

# Define the parameters to iterate over
ne_values = [True, False, "All"]
wer_rates = [round(i * 0.025, 3) for i in range(0, 41)]  # 0.1 to 1.0 with a step of 0.1
# wer_rates = [1]
word_errors = [1,2,3,4,5]

# Generate the configurations
for word_error in word_errors:
    for ne in ne_values:
        for wer_rate in wer_rates:
            CONFIG.append({
                "ne": ne,
                "wer_rate": wer_rate,
                "character_per_word_error": word_error,
                "force": True
            })