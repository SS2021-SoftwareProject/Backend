
pragma solidity >=0.7.0 <0.9.0;

contract Collect{
    modifier ownerInvo{
        require(msg.sender==owner);
        _;   
    }
    
    modifier inTime{
        require(block.timestamp<timeout);
        _;
    }
    
    modifier fundGoalReached{
        require(collectedMoney>=goal);
        _;   
    }
    modifier enough{
        require(msg.value>=1000);
        _;
    }
    
    struct Donator{
        address payable donator;
        uint amount;
    }
    
    address payable owner;
    Donator[] donators;
    Donator  don;
    uint collectedMoney;
    uint goal;
    uint timeout;
    address payable receiver;
    
    function donate() public payable inTime enough{
       collectedMoney += msg.value;
        don =  Donator(payable(msg.sender),msg.value);
       donators.push(don);   
    }
    
    function cashOut() public payable fundGoalReached ownerInvo{
        
        receiver.transfer(collectedMoney);
        selfdestruct(owner);
        
    }
    
    
    constructor (address payable _receiver, uint _goal ,uint durationinday){
        receiver=_receiver;
        timeout=durationinday*84600+block.timestamp;
        goal=_goal;
        owner=payable(msg.sender);
    }
    
    function refund() public ownerInvo{
        uint length = donators.length;
        for(uint i=0; i<length;i++){
            donators[i].donator.transfer(donators[i].amount);     
        }
        
        selfdestruct(owner);
    }
    
}
