import os
import sys

from dotenv import load_dotenv
from google import genai
from google.genai import types

from system_prompt import SYSTEM_PROMPT
from call_function import available_functions, call_function



def main():

    if len(sys.argv) < 2:
        print(f'Usage: {sys.argv[0]} <prompt>')
        sys.exit(1)
    prompt = sys.argv[1]
    verbose = "--verbose" in sys.argv
    load_dotenv()

    api_key = os.environ.get("GEMINI_API_KEY")

    client = genai.Client(api_key=api_key)

    messages = [
        types.Content(role="user", parts=[types.Part(text=prompt)]),
    ]

    for i in range(20):
        response = client.models.generate_content(
            model='gemini-2.0-flash-001',
            contents=messages,
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_PROMPT,
                tools=[available_functions],
            )
        )

        for candidate in response.candidates:
            messages.append(candidate.content)

        if response.function_calls:
            for function_call_part in response.function_calls:
                function_call_result = call_function(function_call_part)
                messages.append(function_call_result)
                if not function_call_result.parts[0].function_response.response:
                    raise Exception("No parts[0].function_response.response")
                elif verbose:
                    print(f"-> {function_call_result.parts[0].function_response.response}")
        else:
            print(response.text)
            break

                
            
    # print(response.text)

    if verbose:
        print(
            f'User prompt: {prompt}\n',
            f'Prompt tokens: {response.usage_metadata.prompt_token_count}\n',
            f'Response tokens: {response.usage_metadata.candidates_token_count}',
            sep="",
        )


if __name__ == "__main__":
    main()