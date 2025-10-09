# def prace_se_seznamem():


#     seznam = [100, 5, 3, 21]

#     seznam[2] *= 2

#     seznam.append(55)

#     seznam.sort()
#     seznam.reverse()


#     print(seznam)

# def vrat_treti_prvek(seznam):
#     if len(seznam) >= 3:
#         return seznam[2]
#     else: 
#         return None
    
def prumer(student):
    return sum(student["znamky"]) / len(student["znamky"])

def naformatuj_text(zak):
    return f"Student:{student['jmeno']} {student['prijmeni']},vek: {student['vek']},obor: {student['obor']},prumer: {prumer(student)}"

if __name__ == "__main__":
#     prace_se_seznamem()
#     vrat_treti_prvek [1,2,3,4,5]

#     cisla = [1,2,3,4,5]
#     print(prumer(cisla))
    
    student = {
    "jmeno": "Jan",
    "prijmeni": "Novak",
    "vek": 22,
    "znamky": [1,2,3,1,2,1]
    }
    student["vek"] += 1
    student["obor"] = "AEFP"
    print(naformatuj_text(student))

