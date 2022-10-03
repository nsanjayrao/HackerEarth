for i in range(int(input())):
    cg,cp=map(int,input().split())
    n=int(input())
    first_solve_count=0
    second_solve_count=0
    for i in range(n):
        first_prob,second_prob=map(int,input().split())
        if first_prob == 1:
            first_solve_count+=1
        if second_prob == 1:
            second_solve_count+=1
    first_prob_prize_cost_green = cg * first_solve_count
    first_prob_prize_cost_purple = cp * first_solve_count
    second_prob_prize_cost_green = cg * second_solve_count
    second_prob_prize_cost_purple = cp * second_solve_count
    
    case_1=first_prob_prize_cost_green + second_prob_prize_cost_purple
    case_2=first_prob_prize_cost_purple + second_prob_prize_cost_green
    print(min(case_1,case_2))
    
