class FrontMiddleBackQueue {
public:
    deque<int> q;

    FrontMiddleBackQueue() {
    }

    void pushFront(int val) {
        q.push_front(val);
    }

    void pushMiddle(int val) {
        int n = q.size();
        q.insert(q.begin() + n / 2, val);
    }

    void pushBack(int val) {
        q.push_back(val);
    }

    int popFront() {
        if (q.empty())
            return -1;

        int val = q.front();
        q.pop_front();
        return val;
    }

    int popMiddle() {
        if (q.empty())
            return -1;

        int n = q.size();
        int index = (n - 1) / 2;

        int val = q[index];
        q.erase(q.begin() + index);

        return val;
    }

    int popBack() {
        if (q.empty())
            return -1;

        int val = q.back();
        q.pop_back();
        return val;
    }
};
/**
 * Your FrontMiddleBackQueue object will be instantiated and called as such:
 * FrontMiddleBackQueue* obj = new FrontMiddleBackQueue();
 * obj->pushFront(val);
 * obj->pushMiddle(val);
 * obj->pushBack(val);
 * int param_4 = obj->popFront();
 * int param_5 = obj->popMiddle();
 * int param_6 = obj->popBack();
 */