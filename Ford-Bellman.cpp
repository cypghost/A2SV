#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    
    // bellman ford
    vector<long long> dist(n + 1, 1e18);
    dist[1] = 0;
    vector<vector<long long>> edges;
    for (int i = 0; i < m; i++) {
        long long u, v, w;
        cin >> u >> v >> w; 
        edges.push_back({u, v, w});
    }
    
    for (int i = 0; i < n - 1; i++) {
        for (auto e : edges) {
            long long u = e[0], v = e[1], w = e[2];
            dist[v] = min(dist[v], dist[u] + w);
        }
    }
    for (int i = 1; i <= n; i++) {
        if (dist[i] != 1e18) 
        {
            cout << dist[i] << " ";
        } else {
            cout << 30000 << " ";
        }
    }
    cout << endl;
    return 0;
}
