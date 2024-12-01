#include <iostream>
#include <vector>
#include <fstream>
#include <algorithm>
#include <unordered_map>


int main(){
    std::vector<int> list1;
    std::vector<int> list2;

    std::ifstream file1("col_1.txt");

    int num = 0;

    while(file1 >> num){
        list1.push_back(num);
    }
    file1.close();
    
    std::sort(list1.begin(),list1.end());

    std::ifstream file2("col_2.txt");
    
    while(file2 >> num){
        list2.push_back(num);
    }

    file2.close();
    std::sort(list2.begin(),list2.end());

    int res = 0;
    for(int i = 0; i<list1.size(); i++){
        res += abs(list1[i] - list2[i]);
    }

    std::cout << "Result of Part 1: " << res << '\n';

    //Part - 2

    std::unordered_map<int,int> freq_dict;

    for(int num:list2){
        freq_dict[num]++;
    }
    int final_res = 0;
    
    for(int num:list1){
        final_res += num * freq_dict[num];
    }

    std::cout << "Final result: " << final_res << '\n';

}