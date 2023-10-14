#include <iostream>
#include <vector>
#include <algorithm>
 
using namespace std;
 
const long long INF = 1e18; // A large value representing infinity
 
int main() {
    int n, m, q;
    cin >> n >> m >> q;    
 
    // Initialize the distance matrix with INF
    long long dist[n + 1][n + 1];
 
    for(int i = 0; i < n + 1; i++) {
        for (int j = 0; j < n + 1; j++) {   
            dist[i][j] = INF;
        }
    }
 
    for (int i = 0; i < m; i++) {
        long long u, v, w;
        cin >> u >> v >> w;
        dist[u][v] = min(dist[u][v], w);
        dist[v][u] = min(dist[v][u], w);
    }
 
    // Set diagonal elements to 0
    for (int i = 1; i <= n; i++) {
        dist[i][i] = 0;
    }
 
    // Floyd-Warshall algorithm to compute shortest distances
    for (int k = 1; k <= n; k++) {
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
            }
        }
    }
 
    // Handle queries
    for (int i = 0; i < q; i++) {
        int u, v;
        cin >> u >> v;
 
        if (dist[u][v] == INF) {
            cout << -1 << endl;
        } else {
            cout << dist[u][v] << endl;
        }
    }
 
    return 0;
}
