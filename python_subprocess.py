import subprocess

if __name__ == "__main__":
    # #basic
    # subprocess.run(["ls", "-itr"])
    # subprocess.run(["python", "python_script101.py", "--x","8"])

    ##use output of subprocess
    sum_xt = 0
    count_round = 0
    for i in range(100):
        if i%2 != 0:
            sum_xt += i*2
            count_round += 1
            process1 = subprocess.Popen(["python", "python_script101.py", "--x", f'{i}'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, err = process1.communicate()

            print("('_>')"*15)            
            print(f'Round {count_round}')
            print(f'x = {i}')
            print(out.decode('utf-8'))

    print("-"*90)
    print(f'Total Round = {count_round}')
    print(f'Total xt = {sum_xt}')



    #HW สั่งรัน python_scritp101.py 50 รอบ โดย x = 1,3,5,7,... 
    #แล้วให้เอา output ของ xt มารวมกันแล้ว print ออกมา


