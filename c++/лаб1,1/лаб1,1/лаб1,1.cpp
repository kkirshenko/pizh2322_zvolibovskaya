#include <iostream>
#include <string>
#include <vector>

using namespace std;

// Класс "Мероприятие" для хранения информации о событии
class Event {
private:
    string date;        // Дата мероприятия в формате "ГГГГ-ММ-ДД"
    string title;       // Название мероприятия
    string description; // Подробное описание

public:
    // Конструктор для инициализации данных
    Event(string d, string t, string desc)
        : date(d), title(t), description(desc) {
    }

    // Геттеры для получения данных
    string getDate() const { return date; }
    string getTitle() const { return title; }
    string getDescription() const { return description; }

    // Сеттеры для изменения данных
    void setDate(string d) { date = d; }
    void setTitle(string t) { title = t; }
    void setDescription(string desc) { description = desc; }

    // Метод для вывода информации о мероприятии
    void display() const {
        cout << "Дата: " << date << endl
            << "Название: " << title << endl
            << "Описание: " << description << endl
            << "--------------------------" << endl;
    }
};

// Класс "Календарь" для управления мероприятиями
class Calendar {
private:
    string roomName;    // Название помещения (например, "Конференц-зал")
    string address;     // Адрес помещения
    vector<Event> events; // Динамический список мероприятий

public:
    // Конструктор для инициализации помещения
    Calendar(string room, string addr)
        : roomName(room), address(addr) {
    }

    // Добавление мероприятия в календарь
    void addEvent(const Event& event) {
        events.push_back(event);
        cout << "Мероприятие добавлено!" << endl;
    }

    // Удаление мероприятия по индексу
    void removeEvent(int index) {
        if (index >= 0 && index < events.size()) {
            events.erase(events.begin() + index);
            cout << "Мероприятие удалено!" << endl;
        }
        else {
            cout << "Ошибка: неверный индекс!" << endl;
        }
    }

    // Вывод всех мероприятий в календаре
    void displayAll() const {
        cout << "\nКалендарь: " << roomName << endl
            << "Адрес: " << address << endl
            << "Список мероприятий:\n";

        for (size_t i = 0; i < events.size(); ++i) {
            cout << "[" << i + 1 << "]" << endl;
            events[i].display();
        }
    }

    // Поиск мероприятий по дате
    void searchByDate(string targetDate) {
        bool found = false;
        for (const auto& event : events) {
            if (event.getDate() == targetDate) {
                event.display();
                found = true;
            }
        }
        if (!found) {
            cout << "Мероприятий на " << targetDate << " не найдено." << endl;
        }
    }
};

int main() {
    setlocale(LC_ALL, "Russian");
    // Создание календаря
    Calendar officeCalendar("Офис 404", "ул. Программистов, 13");

    // Добавление мероприятий
    officeCalendar.addEvent(Event("2023-11-01", "Совещание", "Обсуждение проекта X"));
    officeCalendar.addEvent(Event("2023-11-02", "Митинг", "Планирование квартала"));
    officeCalendar.addEvent(Event("2023-11-01", "Встреча", "Переговоры с клиентом"));

    // Вывод всех мероприятий
    officeCalendar.displayAll();

    // Поиск по дате
    cout << "\nПоиск мероприятий 2023-11-01:" << endl;
    officeCalendar.searchByDate("2023-11-01");

    // Удаление мероприятия
    officeCalendar.removeEvent(1); // Удаляем второе мероприятие (индекс 1)

    // Повторный вывод после удаления
    cout << "\nОбновленный список:" << endl;
    officeCalendar.displayAll();

    return 0;
}