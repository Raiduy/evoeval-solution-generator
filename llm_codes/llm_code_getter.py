from huggingface_hub import get_inference_endpoint, list_inference_endpoints, AsyncInferenceClient

import asyncio
import os

messages = [{"role": "user", "content": "What is the capital of France?"}]

endpoint = get_inference_endpoint("code-millenials-34b-utk")

def get_response():
    print(endpoint.client.chat_completion(messages, max_tokens=100))


if __name__ == '__main__':
    result = endpoint.client.text_generation("How do you make a for loop in python?",
                                             stop_sequences=["\end{code}"],
                                             max_new_tokens=1400)

    #get_response()
    print(result)

