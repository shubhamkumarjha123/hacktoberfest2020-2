#include<iostream>
using namespace std;
int main()
{
    string name;
    int age;
    cout<<"enter your name"<<endl;
    cin>>name;
    cin.ignore(50,'\n');
    cout<<name<<endl;

    cout<<"enter your age"<<endl;
    if(cin>>age)
        cout<<"you entered the age as an integer"<<endl;
    else
    {
        cin.clear();
        cin.ignore(50,'\n');
        cout<<"enter the age in numbers, not in words, enter again"<<endl;
        cin>>age;
    }
    return 0;
