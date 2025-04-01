from academics_data import create_academics_lists

def print_academics():
    physicists, mathematicians = create_academics_lists()
    
    print("\nФизики (по дате избрания):")
    for academic in physicists:
        print(academic)
        
    print("\nМатематики (по дате избрания):")
    for academic in mathematicians:
        print(academic)

if __name__ == "__main__":
    print_academics()
