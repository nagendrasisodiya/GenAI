from model import llama3_response, granite_response, mixtral_response


def call_all_models(system_prompt, user_prompt):
    llama_result=llama3_response(system_prompt, user_prompt)
    granite_result=granite_response(system_prompt, user_prompt)
    mixtral_result=mixtral_response(system_prompt, user_prompt)

    print("llama_result: ", llama_result, "\n")
    print("granite_result: ", granite_result, "\n")
    print("mixtral_result: ", mixtral_result, "\n")

call_all_models("You are a helpful assistant who provides concise and accurate answers",
                "What is the capital of Canada? Tell me a cool fact about it as well")

