import platform


os_info = platform.uname()  


with open("os_info.txt", "w", encoding="utf-8") as file:  
    file.write(f"Система: {os_info.system}\n")  
    file.write(f"Название узла: {os_info.node}\n")  
    file.write(f"Релиз: {os_info.release}\n")  
    file.write(f"Версия: {os_info.version}\n")  
    file.write(f"Архитектура: {os_info.machine}\n")  
    file.write(f"Процессор: {os_info.processor}\n")  

print("Файл os_info.txt создан.")