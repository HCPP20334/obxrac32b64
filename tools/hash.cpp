#include <iostream>
#include <string>
#include <stdint.h>
#include <random>

std::string_view get_mask_string(){
const std::string_view mask = "1234567890qwertyuiopasdfghjklzxcvbnm%$#@&*?/\\";
return mask;
}
uint64_t random(uint64_t t){
 std::random_device random_d;
 std::mt19937_64 mt64;
 mt64.seed(random_d());
 std::uniform_int_distribution<uint64_t> dist(0,UINT64_MAX);
 uint64_t u64_random = dist(mt64);
 uint64_t u64Seed = (t + u64_random);
 u64Seed ^= u64Seed << 16;
 u64Seed ^= u64Seed << 8;
 u64Seed ^= u64Seed >> 4;
 return u64Seed;
}


std::string hash(uint64_t max_len){
std::string out = "";
for(uint64_t _h = 0; _h < max_len;_h++){
out += get_mask_string()[random(_h) % get_mask_string().length()];
}
return out;
}


int main(){
	uint64_t u64Size = 0;
	std::cout <<"hash size:\n";
	std::cin >> u64Size;
	std::cout << hash(u64Size);

}
