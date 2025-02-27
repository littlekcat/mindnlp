# Copyright 2022 Huawei Technologies Co., Ltd
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ============================================================================
"""
tokenizers init
"""

from .basic_tokenizer import BasicTokenizer
from .bert_tokenizer import BertTokenizer
from .gpt2_tokenizer import GPT2Tokenizer
from .t5_tokenizer import T5Tokenizer
from .gpt_tokenizer import GPTTokenizer
from .codegen_tokenizer import CodeGenTokenizer
from .roberta_tokenizer import RobertaTokenizer
from .longformer_tokenizer import LongformerTokenizer
from .nezha_tokenizer import NezhaTokenizer
from .ernie_tokenizer import ErnieTokenizer
from .tinybert_tokenizer import TinyBertTokenizer
from .chatglm_tokenizer import ChatGLMTokenizer
from .bart_tokenizer import BartTokenizer
from .mobilebert_tokenizer import MobileBertTokenizer

__all__ = ['BasicTokenizer', 'BertTokenizer', 'T5Tokenizer', 'GPTTokenizer', 'GPT2Tokenizer', 'ErnieTokenizer', 'CodeGenTokenizer',
           'RobertaTokenizer', 'LongformerTokenizer', 'NezhaTokenizer', 'TinyBertTokenizer', 'ChatGLMTokenizer', 'BartTokenizer',
           'MobileBertTokenizer'
           ]
