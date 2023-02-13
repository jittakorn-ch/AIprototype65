import subprocess

if __name__ == "__main__":
    ##basic
    subprocess.run(["ls", "-itr"])
    subprocess.run(["python", "python_script101.py", "--x","8"])

    ##use output of subprocess
    process1 = subprocess.Popen(["python", "python_script101.py", "--x","8"],stdout=subprocess)
    out, err = process1.communicate()
    print(out.decode('utf-8'))


    #HW สั่งรัน python_scritp101.py 50 รอบ โดย x = 1,3,5,7,... 
    #แล้วให้เอา output ของ xt มารวมกันแล้ว print ออกมา