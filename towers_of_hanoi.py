# Pseudocode
# 1) get no of disks from user
# 2) name the towers as source auxilary destination
# 3) move smaller disks to auxilary
# 4) move the largest disk to destination
# 5) move smaller disks from auxilary to destination

disks = int(input("Enter the number of disks on the first tower: "))
count = 0


def towers_of_hanoi(disks, src, aux, dest):
    global count
    if disks == 1:
        print(f"Move disk {disks} from {src} to {dest}")
    else:
        towers_of_hanoi(disks-1, src, dest, aux)
        count += 1
        print(f"Move disk {disks} from {src} to {dest}")
        towers_of_hanoi(disks-1, aux, src, dest)


towers_of_hanoi(disks, "Tower 1", "Tower 2", "Tower 3")
