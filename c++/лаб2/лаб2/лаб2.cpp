#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Event {
private:
    string date;
    string title;
    string description;

public:
    Event(string d, string t, string desc)
        : date(d), title(t), description(desc) {
    }

    string getDate() const { return date; }
    string getTitle() const { return title; }
    string getDescription() const { return description; }

    void display() const {
        cout << "Дата: " << date << endl
            << "Название: " << title << endl
            << "Описание: " << description << endl
            << "--------------------------" << endl;
    }
};

class Calendar {
private:
    string roomName;
    string address;
    vector<Event> events;

public:
    Calendar(string room, string addr)
        : roomName(room), address(addr) {
    }

    // Новый метод для создания и добавления мероприятия
    void addCustomEvent(string date, string title, string description) {
        Event newEvent(date, title, description);  // Создание объекта
        events.push_back(newEvent);                // Добавление в массив
        cout << "Новое мероприятие создано и добавлено!" << endl;
    }

    void displayAll() const {
        cout << "\nКалендарь: " << roomName << endl
            << "Адрес: " << address << endl
            << "Список мероприятий:\n";

        for (size_t i = 0; i < events.size(); ++i) {
            cout << "[" << i + 1 << "]" << endl;
            events[i].display();
        }
    }
};

int main() {
    Calendar officeCalendar("Офис 404", "ул. Программистов, 13");

    // Использование нового метода
    officeCalendar.addCustomEvent("2023-12-01", "Новый год", "Подготовка к празднику");
    officeCalendar.addCustomEvent("2023-12-15", "Корпоратив", "Ежегодная вечеринка");

    officeCalendar.displayAll();

    return 0;
}