# Лабораторная №1: Первичная инициализация
# Курс: Основы теории систем
# Студент: Силаева Софья Игоревна

def get_system_info():
    system_info = {
        "student_name": "Силаева Софья Игоревна",
        "academic_group": "ИВТИИбд-12",
        "github_link": "https://github.com/SilaevaSofia"
    }
    return system_info

if __name__ == "__main__":
    info = get_system_info()
    print("Информация о системе:")
    for key, value in info.items():
        print(f"- {key}: {value}")
