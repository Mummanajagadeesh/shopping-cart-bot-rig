from inference_sdk import InferenceHTTPClient

CLIENT = InferenceHTTPClient(
    api_url="https://detect.roboflow.com",
    api_key="W7Zp10EM8b5983DIhfmz"
)

result = CLIENT.infer("cd00481a3e82cb99590517fe7ab2c87f.jpeg", model_id="groceries-6pfog/6")