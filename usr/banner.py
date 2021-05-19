C = "\033[94;m"
G = "\033[92;m"
r = "\033[0;m"
P = "\033[93;m"
def banner():
    print("""
    {0}╔╦╗╔═╗╦  ╔═╗╦╔═╔═╗ 
║║║╠═╣║  ╠═╣╠╩╗║ ║ 
╩ ╩╩ ╩╩═╝╩ ╩╩ ╩╚═╝ 
╔═╗╔╗╔╦╔═╗╔═╗╦═╗╔═╗
╚═╗║║║║╠═╝║╣ ╠╦╝║ ║
╚═╝╝╚╝╩╩  ╚═╝╩╚═╚═╝{2}1.1{0}dev.
 {1}[ {2}Simple Multi-Bruteforce{1} ]{1} 
 {1} [ {2}Recode by : me{1} ]{1}
            """.format(C,r,G))
def menu():
    print(f"{C}1{r} Dump Pertemanan")
    print(f"{C}2{r} Dump dari Like Post")
    print(f"{C}3{r} Dump dari Pencarian")
    print(f"{C}4{r} Grup Publik (Hanya bisa 100 User)")
    print(f"{C}5{r} Dump Publik")
    print(f"{C}6{r} Dari Hastag")
    print(f"{C}7{r} Lihat Hasil Crack")

