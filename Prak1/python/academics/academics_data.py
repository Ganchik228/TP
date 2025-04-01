from academic import Academic, CircularList

def create_academics_lists():
    academics_data = [
        ("Петров А.И.", "физика", "12.05.1980"),
        ("Иванов Б.С.", "математика", "03.11.1975"), 
        ("Сидоров В.К.", "физика", "28.02.1990"),
        ("Кузнецов Г.М.", "математика", "15.07.1985")
    ]
    
    physicists = CircularList()
    mathematicians = CircularList()
    
    for name, field, date in academics_data:
        academic = Academic(name, field, date)
        if field == "физика":
            physicists.append(academic)
        elif field == "математика":
            mathematicians.append(academic)
            
    physicists.sort_by_election_date()
    mathematicians.sort_by_election_date()
    
    return physicists, mathematicians
