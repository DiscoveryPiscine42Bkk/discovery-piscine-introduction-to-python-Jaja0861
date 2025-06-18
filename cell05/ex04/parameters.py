def show_parameters(*args):
    print(f"Number of parameters received: {len(args)}")
     print("Parameters received:", args)
     show_parameters(1, 2, 3, 5, 7, 9)