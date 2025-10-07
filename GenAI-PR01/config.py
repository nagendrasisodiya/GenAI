from ibm_watsonx_ai.metanames import GenTextParamsMetaNames

# Model parameters
# The params object defines the key settings for how the LLM generates its output. Here's what we're adjusting:
#
# DECODING_METHOD: This controls how the LLM selects its next token.
# The default is greedy decoding, where the model always picks the most probable next token.
# Alternatively, setting this to sampling lets you influence the randomness of the model's choices (with temperature being a key factor to tweak). If you want more deterministic, predictable responses, use greedy.
#
# MAX_NEW_TOKENS: This sets the maximum number of tokens the LLM can generate in a response.
# Since both input and output tokens typically contribute to the cost of using the model, this parameter is important for managing usage.
# Here, we're limiting the output to 100 new tokens.
#
# You may be asking yourself, "What is a token?"
# It is a small unit of text, which can be as short as a single character,
#  part of a word, or even an entire word, depending on the language model's tokenizer.
# When an LLM processes text, it breaks the input down into these tokens to understand and generate a response
PARAMETERS = {
    GenTextParamsMetaNames.DECODING_METHOD: "greedy",
    GenTextParamsMetaNames.MAX_NEW_TOKENS: 250
}
# watsonx credentials
CREDENTIALS = {
    "url":
    "api_key":
    "project_id":
}
# Model IDs
LLAMA3_MODEL_ID = "meta-llama/llama-3-2-11b-vision-instruct"
GRANITE_MODEL_ID = "ibm/granite-3-8b-instruct"
MIXTRAL_MODEL_ID = "mistralai/mistral-large"
