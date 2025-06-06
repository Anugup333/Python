def towerofHanoi(n, sou, hel, des):
    if n == 1:
        print(f"Transfer disk {n} from {sou} to {des}")
        return
    towerofHanoi(n-1, sou, des, hel)
    print(f"Transfer disk {n} from {sou} to {des}")
    towerofHanoi(n-1, hel, sou, des)


n = 3
towerofHanoi(n, "S", "H", "D")