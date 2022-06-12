'''
Sample TestCase 1
Input
2
3
8
50 70 30 100 80 20 150 10
4
6
10 20 32 412 500 11'''

def get_minimum_price(dicts:dict):
    sum_list = []
    ans=0
    for key,value in dicts.items():
        value.sort()
        if key!=0 or key >1:
            for j in value[0:key]:
                ans+=j
            sum_list.append(ans)
            ans = 0
        else: sum_list.append(0)

    return sum_list

if __name__=="__main__":
    user_input = int(input())
    lists = {}
    string = ""
    i=0
    while i<user_input:
        user_gift = int(input())
        shop_gift = int(input())
        for _ in input().split(" "):
            string+=_+" "
        new_lists = string.strip().split(" ")
        lists[user_gift] = list(map(int,new_lists[0:shop_gift]))
        string= ""
        i+=1
    
    get_lists = get_minimum_price(lists)
    for i in get_lists:
        print(i)


        
