package wesayallright.timemanager.InnerLayer.LocalFile;

import org.w3c.dom.Document;

import wesayallright.timemanager.InnerLayer.exception.WrongID;

/**
 * Created by mj on 17-4-16.
 * 文件类，所有对文件的操作均通过此类实现
 */

public class LocalFile extends java.io.File{
    private static String workPath;
    // 本程序执行时的位置，由MainActivity获取
    public LocalFile(String fname) {
        super(workPath + "/" + fname);
        // holy shit。按编号分文件夹！
    }

    static public void setCwd(String cwd) {
        workPath = cwd;
    }

    public Document parseXML() {
        return new DOMParser().parse(this);
    }

    public static LocalFile loadUser(String userId) throws WrongID {
        if (userId.charAt(0) != 'U') {
            throw new WrongID(userId);
        }
        return new LocalFile(workPath + "/" + "users" + "/" + "user_" + userId + ".xml");
    }

    public static LocalFile loadCalendar(String userId) throws WrongID {
        if (userId.charAt(0) != 'U') {
            throw new WrongID(userId);
        }
        return new LocalFile(workPath + "/" + "calendars" + "/" + "cal_" + userId + ".xml");
    }

    public static LocalFile loadGroups(String userId) throws WrongID {
        if (userId.charAt(0) != 'U') {
            throw new WrongID(userId);
        }
        return new LocalFile(workPath + "/" + "groupList" + "/" + "gpl_" + userId + ".xml");
    }

}