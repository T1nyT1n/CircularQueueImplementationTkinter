// g++ -shared -fPIC -o libqueue.so queue.cpp (Linux)
// cl /LD queue.cpp /Fequeue.dll (Windows)

#include <cstdlib>
#include <cstring>
#include <string>

extern "C" {

struct ListItem {
    int data;
    ListItem* next;
};

ListItem* head = nullptr;
ListItem* tail = nullptr;
int count = 0;

bool EmptyQueue() {
    return tail == nullptr;
}

int ReadElement() {
    if (head != nullptr)
        return head->data;
    else
        return -1;
}

void PushElement(int data_to_insert) {
    ListItem* new_item = new ListItem{data_to_insert, head};
    if (EmptyQueue()) {
        new_item->next = new_item;
        tail = new_item;
        head = new_item;
    } else {
        tail->next = new_item;
        tail = new_item;
    }
    count++;
}

int PopElement() {
    if (!EmptyQueue()) {
        ListItem* temp = head;
        int value = temp->data;
        if (tail == head) {
            head = nullptr;
            tail = nullptr;
        } else {
            head = head->next;
            tail->next = head;
        }
        delete temp;
        count--;
        return value;
    }
    return -1;
}

int ClearQueue() {
    if (!EmptyQueue()) {
        int removed = 0;
        while (!EmptyQueue()) {
            PopElement();
            removed++;
        }
        return removed;
    }
    return -1;
}

char* ShowAllElements() {
    if (EmptyQueue())
        return nullptr; // в Python будет восприниматься как None

    std::string result;
    ListItem* current = head;
    while (current->next != head) {
        result += std::to_string(current->data);
        result += ", ";
        current = current->next;
    }
    result += std::to_string(current -> data);   // последний элемент

    char* cstr = (char*)malloc(result.size() + 1);
    std::strcpy(cstr, result.c_str());
    return cstr;
}

int RemoveElementsByCondition(int condition, int num) {
    if (!EmptyQueue()) {
        int initial_count = count;
        for (int i = 0; i < initial_count; ++i) {
            int current_data = ReadElement();
            PopElement();
            if ((condition == 0 && current_data >= num) ||
                (condition == 1 && current_data <= num) ||
                (condition == 2 && current_data != num)) {
                PushElement(current_data);
            }
        }
        return 0;
    }
    return -1;
}

void FreeCString(void* str) {
    free(str);
}

} // extern "C"