function mode(arr)
{
    arr.sort(function(a,b){return a-b});
    var count = 0;
    var maxCount = 0;
    var number = 0;
    var answer = [];
    for(var i = 0; i <arr.length; i++)
    {
        if(arr[i] != arr[i+1] && count>=maxCount)
        {
            maxCount = count;
            number = arr[i];
        }
        else if(arr[i] == arr[i+1])
        {
            count++;
        }
        if(arr[i] != arr[i+1])
        {
            count = 0;
        }
    }
    for(var i = 0; i < arr.length; i++)
    {
        if(arr[i] != arr[i+1])
        {
            if(count == maxCount)
            {
                answer.push(arr[i]);
            }
        }
        else if(arr[i] == arr[i+1])
        {
            count++;
        }
        if(arr[i] != arr[i+1])
        {
            count = 0;
        }
    }
    return answer;
}

var T1 = [4, 5, 1, 3, 5, 8, 9, 10, 4, 4, 5, 1, 2];


console.log(mode(T1));