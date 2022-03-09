boolean solution(double[] prices, String[] notes, double x) {
    float updatedPrice=0;
      for(int i = 0; i < notes.length; i++)
      {
          //split the notes into each word
          String[] str = notes[i].split(" ");
          float change = 0;
          //if first word is same then do not update the value of change
          if(str[0].equals("Same"))
          {
              change = 0;
          }
          else
          {
              //for higher price
              if(str[1].equals("higher"))
              {
                  //use split method to find out the percentage
                  String[] temp = str[0].split("%");
                  change = Float.parseFloat(temp[0]);
              }
              //for lower price
              else
              {
                  String[] temp = str[0].split("%");
                  change = Float.parseFloat(temp[0]);
                  //convert change to negative to show that it's negative in nature
                  change = change*-1;
              }
          }
          //find the updated change for each price
          updatedPrice += prices[i] - ((prices[i]* 100)/(100 + change));
      }
      //check if overall update change is greater than x or not
      if(updatedPrice > x)
          return false;
      else
          return true;
}
