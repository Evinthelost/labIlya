import json

def json_string_to_dict(json_str):
    try:
        
        data_dict = json.loads(json_str)
        return data_dict
    except json.JSONDecodeError as e:
       
        print(f"Ошибка при декодировании JSON: {e}")
        return None


json_string = '{"name": "Ilya", "age": 20, "city": "MMRK"}'

result = json_string_to_dict(json_string)

print(result)
