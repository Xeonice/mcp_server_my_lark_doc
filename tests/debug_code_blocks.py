import sys
import json
from pprint import pprint
from collections import OrderedDict
sys.path.insert(0, '.')
from mcp_lark_doc_manage.markdown_converter import convert_markdown_to_blocks
from tests.markdown_conversion.conftest import load_test_data, load_expected_result

markdown = load_test_data('lists.md')
expected = load_expected_result('lists_result.json')
result = convert_markdown_to_blocks(markdown)

print('Type of result:', json.dumps(result, indent=4))
# 将结果输出到本地 json 文件
with open('debug_code_blocks_result.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, indent=4, ensure_ascii=False)

# 将期望结果也输出到本地 json 文件以便比较
with open('debug_code_blocks_expected.json', 'w', encoding='utf-8') as f:
    json.dump(expected, f, indent=4, ensure_ascii=False)

print(f"Results saved to 'debug_code_blocks_result.json' and 'debug_code_blocks_expected.json'")

print('Type of expected:', json.dumps(expected, indent=4))
