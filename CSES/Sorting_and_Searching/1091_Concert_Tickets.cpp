#include <iostream>
#include <set>
 
int main() {
    int n, m, h, t;
    std::cin >> n >> m;
    std::multiset<int> ms;
    std::multiset<int>::iterator it;
    for (int i = 0; i < n; ++i) {
        std::cin >> h;
        ms.insert(h);
    }
    for (int i = 0; i < m; ++i) {
        std::cin >> t;
        it = ms.upper_bound(t);
        if (it == ms.begin()) {
            std::cout << -1 << "\n";
        } else {
            std::cout << *(--it) << "\n";
            ms.erase(it);
        }
    }
    return 0;
}
