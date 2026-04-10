#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Basit Yapılacaklar Listesi Uygulaması

tasks = []

def show_menu():
    """Menüyü göster"""
    print("\n" + "="*40)
    print("📝 YAPILACAKLAR LİSTESİ")
    print("="*40)
    print("1. Görev Ekle")
    print("2. Görevleri Listele")
    print("3. Görevi Tamamla")
    print("4. Görevi Sil")
    print("5. Çıkış")
    print("="*40)

def add_task():
    """Yeni görev ekle"""
    task = input("\n➕ Yeni görev girin: ").strip()
    if task:
        tasks.append({"görev": task, "tamamlandı": False})
        print(f"✅ '{task}' eklendi!")
    else:
        print("❌ Boş görev eklenemez!")

def list_tasks():
    """Tüm görevleri listele"""
    if not tasks:
        print("\n📭 Henüz görev yok!")
        return
    
    print("\n📋 GÖREVLERİNİZ:")
    print("-" * 40)
    for i, task in enumerate(tasks, 1):
        status = "✓" if task["tamamlandı"] else "○"
        print(f"{i}. [{status}] {task['görev']}")
    print("-" * 40)

def complete_task():
    """Görevi tamamla"""
    list_tasks()
    if not tasks:
        return
    
    try:
        num = int(input("\n✔️ Hangi görev tamamlandı? (numara): "))
        if 1 <= num <= len(tasks):
            tasks[num-1]["tamamlandı"] = True
            print(f"✅ Görev tamamlandı!")
        else:
            print("❌ Geçersiz numara!")
    except ValueError:
        print("❌ Lütfen geçerli bir numara girin!")

def delete_task():
    """Görevi sil"""
    list_tasks()
    if not tasks:
        return
    
    try:
        num = int(input("\n🗑️ Hangi görevi silmek istiyorsun? (numara): "))
        if 1 <= num <= len(tasks):
            silinen = tasks.pop(num-1)
            print(f"🗑️ '{silinen['görev']}' silindi!")
        else:
            print("❌ Geçersiz numara!")
    except ValueError:
        print("❌ Lütfen geçerli bir numara girin!")

def main():
    """Ana program"""
    print("\n🎉 Yapılacaklar Listesine Hoş Geldiniz!")
    
    while True:
        show_menu()
        choice = input("Seçim yapın (1-5): ").strip()
        
        if choice == "1":
            add_task()
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("\n👋 Hoşça kalın!")
            break
        else:
            print("❌ Geçersiz seçim! Lütfen 1-5 arasında seçin.")

if __name__ == "__main__":
    main()
