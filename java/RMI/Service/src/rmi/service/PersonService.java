package rmi.service;

import java.rmi.Remote;
import java.rmi.RemoteException;
import java.util.List;
import rmi.model.*;

//此为远程对象调用的接口，必须继承Remote类
public interface PersonService extends Remote {
    public List<PersonEntity> GetList() throws RemoteException;
}
