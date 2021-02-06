//Author- Monika Chauhan
#include<iostream>

using namespace std;
 char board[3][3]={{'1','2','3'},{'4','5','6'},{'7','8','9'}};
 char currentMarker;
 int currentPlayer;
 void drawboard()
 {
     cout<<" "<<board[0][0]<<" | "<<board[0][1]<<" | "<<board[0][2]<<" | "<<endl;
     cout<<"------------"<<endl;
      cout<<" "<<board[1][0]<<" | "<<board[1][1]<<" | "<<board[1][2]<<" | "<<endl;
      cout<<"------------"<<endl;
       cout<<" "<<board[2][0]<<" | "<<board[2][1]<<" | "<<board[2][2]<<" | "<<endl;
 }
 void placeMarker(int slot)
 {
     int row;
     if(slot%3==0 )
     row=(slot/3)-1;
     else 
     row= slot/3;

     int col;
     if(slot%3==0)
     col=2;
     else
     col=(slot%3)-1;

     board[row][col]=currentMarker;
 }
int win()
{
    for(int i=0; i<3; i++)
    {
        if(board[i][0]==board[i][1] && board[i][1]==board[i][2])
        return currentPlayer;
        if(board[0][i]==board[1][i] && board[1][i]==board[2][i])
        return currentPlayer;
        if(board[0][0]==board[1][1] && board[1][1]==board[2][2])
         return currentPlayer;
         if(board[0][2]==board[1][1] && board[1][1]==board[2][0])
         return currentPlayer;



    }
    return 0;
}
void swap()
{

if(currentMarker=='X')
currentMarker='O';
else
{
    currentMarker='X';
}
if(currentPlayer==1)
currentPlayer=2;
else
{
    currentPlayer=1;
}


}
void game()
{
    cout<<"PLAYER 1, CHOOSE YOUR MARKER";
    char markerP;
    cin>> markerP;

    currentPlayer=1;
    currentMarker= markerP;
    drawboard();

    int playerwon;
    for(int i=0; i<9 ; i++)
    {
        cout<<"It's player"<<currentPlayer<<"'s turn, Enter ur slot:";
        int slot;
        cin>>slot;

        placeMarker(slot);
         drawboard();
        playerwon=win();

        if(playerwon==1)
        cout<<"PLAYER 1 WON! CONGRATULATIONS!";

        if(playerwon==2)
        cout<<"PLAYER 2 WON! CONGRATULATIONS!";

    swap();
       
    }
if(playerwon==0)
cout<<"that'a a tie";

}
 int main()
 {   
     game();
 }