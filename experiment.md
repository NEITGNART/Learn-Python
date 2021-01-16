
#include <iostream>
#include <functional>

using namespace std;

int a[100];
bool visited[100];
int n;

void print() {

    for (int j = 1; j <= n; ++j) {
            cout << a[j] << ' ';
        }
        cout << '\n';
}

static int cnt = 0;


void Try(int i) {
    

    for (int j = 0; j <= 1; ++j) {
        
        a[i] = j;

        if (i == n) {
            ++cnt;    
            print();
        }
        else {
            Try(i+1);
        }
    }

}


int main(void) {

    n = 10;
    Try(1);
    
    cout << cnt << endl;
    return 0;
}



            1 số lưu ý về hàm backtrack rút ra trong việc code
            có 2 cách đặt if (đặt đầu hoặc đặt cuối). Ví dụ như cách đặt  
            void Try(int i) {                 
            if (...)                
            for_each in ...
            }
            HOẶC   
            void Try(int i) {
                for_each in ... 
                    if (...)
            }
            nên mặc định chọn cách 2 và khi làm backtracking nên lấy chỉ số index  = 1 trong mọi tình huống
            còn không thì rất nên cẩn thận vì có thể bị stackoverflow bất cứ lúc nào

            NOTE: nếu khi dùng if loại 1 thì trong hàm (i == n) phải tăng thành n + 1 Với (i == n + 1) như này
            còn if loại 2 thì không
            NOTE: nếu khi dùng if loại 2 thì khi gọi hàm Try(i + 1) phải đi kèm với else với if ở trên
            bởi vì if else đó được dùng làm điều kiện dừng luôn (backtracking là đệ quy nhiều for nên phải có đk dừng)

            cách tính số lần lặp với thuật toán sinh nhị phân số đáp án sẽ vừa khít 2 ^ n
            vì thế chỉ cần for từ  0 tới 1 sẽ là 2 đơn vị -> 2 ^ n
            với cách tính số giai thừa thì for từ 1 -> n và điều kiện dừng là i == n sẽ tốn hết n ^ n
            không gian n ^ n lớn hơn rất nhiều so với không gian n!
            NOTE: khi làm giai thừa cần dùng thêm 1 mảng bool để check condition

            với cách tính subset thì phải đi từ x[i-1] -> n - k + i ( Hiện tại thì trình mình chưa đủ để hình dung)
            hy vọng sẽ quay trở lại để hoành thành đoạn note




