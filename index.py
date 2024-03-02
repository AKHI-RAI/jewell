class dashboard:
    def __init__(self, root):
        self.root=root
        self.root.title("Jewellery Management System")
        self.root.geometry("1500x800+0+0")


if __name__=="__main__":
    root=Tk()
    obj=dashboard(root)

    root.mainloop()
