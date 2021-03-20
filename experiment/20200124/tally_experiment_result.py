import csv
import sys
from dataclasses import dataclass
from typing import Tuple, Dict

@dataclass
class Eval:
    eval_name: str # 
    total: int # 合計
    avg: float # 平均
    n_item: int # 現在何個か合計している

rating_dict = {
    "強くそう思わない" : 1,
    "そう思わない" : 2,
    "わからない" : 3,
    "そう思う" : 4,
    "強くそう思う" : 5
}

CSV_METHOD1_RELATIONSHIP_BEGIN_INDEX = 2
CSV_METHOD1_UNDERSTANDABLE_BEGIN_INDEX = 3
CSV_METHOD1_NOVELTY_BEGIN_INDEX = 4
CSV_METHOD2_RELATIONSHIP_BEGIN_INDEX = 5
CSV_METHOD2_UNDERSTANDABLE_BEGIN_INDEX = 6
CSV_METHOD2_NOVELTY_BEGIN_INDEX = 7

RESULT_TUPLE_RELATIONSHIP_INDEX = 0
RESULT_TUPLE_UNDERSTANDABLE_INDEX = 1
RESULT_TUPLE_NOVELTY_INDEX = 2

def print_result(result_tuplee):
    for ev in result_tuplee:
        print("[{}]".format(ev.eval_name))
        print("total: {}".format(ev.total))
        print("n_item: {}".format(ev.n_item))
        print("avg: {}".format(ev.avg))

def calc(result_tuple, tuple_index: int, item: str):
    result_tuple[tuple_index].total += rating_dict[item]
    result_tuple[tuple_index].n_item += 1
    result_tuple[tuple_index].avg = result_tuple[tuple_index].total / result_tuple[tuple_index].n_item

def has_remainder(begin_index: int, index: int):
    return (index + 6 - begin_index) % 6 == 0

def taliy(path: str):

    method_1_total_and_avg = (
        Eval("relationship", 0, 0.0, 0), 
        Eval("understandable", 0, 0.0, 0), 
        Eval("novelty", 0, 0.0, 0) 
    )

    method_2_total_and_avg = (
        Eval("relationship", 0, 0.0, 0), 
        Eval("understandable", 0, 0.0, 0), 
        Eval("novelty", 0, 0.0, 0) 
    )

    with open(path) as f:
        reader = csv.reader(f)
        _ = next(reader) # タイトル読み飛ばし
        for row in reader:
            for index, item in enumerate(row):
                if(index == 0 or index == 1):
                    continue
                method_count = 0
                # 手法1
                if has_remainder(CSV_METHOD1_RELATIONSHIP_BEGIN_INDEX, index):
                    # relationship
                    calc(method_1_total_and_avg, RESULT_TUPLE_RELATIONSHIP_INDEX, item)
                elif has_remainder(CSV_METHOD1_UNDERSTANDABLE_BEGIN_INDEX, index):
                    # understandable
                    calc(method_1_total_and_avg, RESULT_TUPLE_UNDERSTANDABLE_INDEX, item)
                elif has_remainder(CSV_METHOD1_NOVELTY_BEGIN_INDEX, index):
                    # novelty
                    calc(method_1_total_and_avg, RESULT_TUPLE_NOVELTY_INDEX, item)
                    
                # 手法2
                elif has_remainder(CSV_METHOD2_RELATIONSHIP_BEGIN_INDEX, index):
                    # relationship
                    calc(method_2_total_and_avg, RESULT_TUPLE_RELATIONSHIP_INDEX, item)
                elif has_remainder(CSV_METHOD2_UNDERSTANDABLE_BEGIN_INDEX, index):
                    # understandable
                    calc(method_2_total_and_avg, RESULT_TUPLE_UNDERSTANDABLE_INDEX, item)
                elif has_remainder(CSV_METHOD2_NOVELTY_BEGIN_INDEX, index):
                    # novelty
                    calc(method_2_total_and_avg, RESULT_TUPLE_NOVELTY_INDEX, item)
                    

    return method_1_total_and_avg, method_2_total_and_avg

                

if __name__ == '__main__':
    path = sys.argv[1] 
    method1_result, method2_result = taliy(path)
    print("手法1 結果")
    print_result(method1_result)
    print("手法2 結果")
    print_result(method2_result)
