
#define Maxn 500007
#define Mod 1000000007
#define int long long
namespace maths{
	int gcd(int x, int y){return y ? gcd(y, x % y) : x;}
	
	int fc[Maxn], inv[Maxn], miu[Maxn], phi[Maxn], pr[Maxn];
	bool visp[Maxn];
	int qpow(int u, int v) {
		int ans = 1;
	    for (; v; v >>= 1) {
	        if (v & 1)
	            (ans *= u) %= Mod;
	        (u *= u) %= Mod;
	    }
	    return ans % Mod;
	}
	int mul(int u, int v) {
		int res = 0;
		for (; v; v >>= 1) {
			if(v & 1) res = (res + u) % Mod;
			u = (u + u) % Mod;
		}
		return res;
	}
	void prefac(int s){
 		for (int i = 0; i <= s; i ++){
        	fc[i] = (i == 0) ? 1 : (fc[i - 1] * i % Mod);
    	}		
	}
	void prephimiup(int s) {
		int top = 0;
	    phi[1] = miu[1] = 1;
	     for(int i = 2; i <= s; i++) {
	         if(! visp[i]) {
	             pr[++ top] = i;
	             miu[i] = -1;
	             phi[i] = i - 1;
	         }
	         for(int j = 1; j <= top && i * pr[j] <= s; j++) {
	             visp[i * pr[j]] = 1;
	             if(i % pr[j] == 0) {
	                 phi[i * pr[j]] = phi[i] * pr[j]; /// miu[i * p[j]] = 0
	                 break;
	             }
	             miu[i * pr[j]] = - miu[i]; /// get miu phi when visit 
	             phi[i * pr[j]] = phi[i] * (pr[j] - 1); 
	         }
	     }
	     return;
	 }
	
	void prefcinv(int s){
    	inv[s] = qpow(fc[s], Mod - 2);
    	for (int i = s - 1; i >= 0; i --) 
    		inv[i] = (inv[i + 1] * (i + 1)) % Mod;		
	}
	   
	int C(int u, int v) {
	    if (v > u)
	        return 0;
	    else
	        return fc[u] * inv[v] % Mod * inv[u - v] % Mod;
	}
} // namespace maths