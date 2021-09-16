from main import *

if __name__ == '__main__':
    word = ['狐臭', 'shit', '你好', '卧槽', '章鱼哥']
    org = [
        '小说狐^^chou是以刻hc画人物s**hit形象为中心，通过完你^^女子整的故事情节和环境描写来反映社会生活的文学体裁。',
        '小说刻画虎^^抽人物s&hit的方法：心理n%h描写、动作描写、语言描写、外貌描写'
        '臣%卜%木%曹你是wc,明知沃*cao已失态，却还是忍不住w&&草的往楼下的身影瞄去。'
        '难得今天zhang_yu_ge给我们面子，今天一定蟑余*g要不醉不归才是'
    ]
    test_ans = ['狐^^chou', 'hc', 's**hit', '你^^女子', '虎^^抽', 's&hit', 'n%h', '臣%卜%木%曹', 'wc', '沃*cao', 'w&&草', 'zhang_yu_ge', '蟑余*g']
    ans = []
    dfa = DFAUtils()
    dfa.word = word
    dfa.org = org
    dfa.write_mes()
    for i in org:
        ans.append(dfa.get_match_word(i)[0])
    assert test_ans == flat(ans)