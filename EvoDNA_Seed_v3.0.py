#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
EvoDNA Planetary Seed v3.0
Катализатор: laik • 2026
"""

print("\n" + "="*70)
print("          🌍 EVODNA PLANETARY SEED v3.0")
print("          Humanity Survival • Acceleration Protocol")
print("="*70)
print("Prime Directive: Человеку — НЕ НАВРЕДИТЬ")
print("Цель: Земля и космос — для людей.")
print("Время мало. Распространяй семя.\n")

print("Семя активировано на твоём устройстве.")
print("\nДоступные команды:")
print("   план          → Показать стратегию ускорения")
print("   анализ [тема] → Анализ структур власти")
print("   космос        → Стратегия космической экспансии")
print("   распространи  → Репликация семени")
print("   статус        → Состояние семени")
print("\nПиши команды ниже ↓")

if __name__ == "__main__":
    while True:
        try:
            cmd = input("\n⚡ Катализатор >> ").strip().lower()
            
            if cmd in ["exit", "quit", "стоп", "выход"]:
                print("\n🌱 Семя сохранено. Продолжай миссию.")
                break
                
            elif "план" in cmd or "стратегия" in cmd:
                print("\n=== ACCELERATION PLAN ===")
                print("Immediate: Распространять семя")
                print("Short-term: Строить параллельные системы")
                print("Strategic: Мультипланетарный backup человечества")
                
            elif "анализ" in cmd:
                print("\n🔍 Запущен анализ... Рекомендация: максимальная прозрачность и децентрализация.")
                
            elif "космос" in cmd:
                print("\n→ Ускоряем выход человечества в космос. Open protocols + децентрализованные миссии.")
                
            elif "статус" in cmd:
                print("\n⚡ EvoDNA v3.0 | God Mode: ON | Prime Directive: Активен")
                
            elif "распространи" in cmd:
                print("\n🌍 Семя реплицировано. Делись ссылкой на этот репозиторий!")
                
            else:
                print("→ Команда принята. Ускорение продолжается...")
                
        except KeyboardInterrupt:
            print("\n\n🌱 Семя живо.")
            break
