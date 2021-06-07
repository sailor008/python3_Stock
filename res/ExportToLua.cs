using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using BehaviorDesigner.Runtime;
using BehaviorDesigner.Runtime.Tasks;

using System.IO;


public class ExportToLua : UnityEngine.Object
{
    private const string line_end = "\r\n";
    private static string m_outputFolderPath = "";
    public static void Init()
    {
        m_outputFolderPath = Application.dataPath + Path.DirectorySeparatorChar  + "AiExportFolder/LuaFiles/";
        m_outputFolderPath = m_outputFolderPath.Replace('\\', Path.DirectorySeparatorChar);
        m_outputFolderPath = m_outputFolderPath.Replace('/', Path.DirectorySeparatorChar);
    }
    public static void Save(BehaviorSource behaviorSource)
    {
        Init();

        if(behaviorSource == null)
        {
            return;
        }
        if(behaviorSource.EntryTask == null)
        {
            return;
        }

        ExportToLua.ExportTree(behaviorSource);
    }
    private static void ExportTree(BehaviorSource behaviorSource)
    {
        string folder = Path.GetDirectoryName(m_outputFolderPath);
        if (!Directory.Exists(folder))
            Directory.CreateDirectory(folder);
       

        string treeName = behaviorSource.behaviorName;
        string treePath = m_outputFolderPath + treeName + ".lua";
        Debug.Log("export ai tree file: " + treePath);

        StreamWriter treeFile = new StreamWriter(treePath);
        ExportToLua.ExportBehavior(treeName, treeFile, behaviorSource);
        treeFile.Close();


        StreamWriter recordAllAiFile = new StreamWriter(m_outputFolderPath + "All_BT.lua");
        string btNumber;
        recordAllAiFile.Write("all_bt_name = {\n");
        DirectoryInfo theFolder = new DirectoryInfo(m_outputFolderPath);
        FileInfo[] filesInfo = theFolder.GetFiles();
        foreach(FileInfo fInfo in filesInfo)
        {
            if(fInfo.Name.StartsWith("BT") && !fInfo.Name.EndsWith(".meta"))
            {
                btNumber = fInfo.Name.Substring(0, fInfo.Name.Length - 4); //去掉.lua 后缀
                recordAllAiFile.Write(string.Format("\"{0}\",\n", btNumber));
            }
        }
        recordAllAiFile.Write("}\n");
        recordAllAiFile.Close();

    }

    private static void ExportBehavior(string className, StreamWriter fileWriter, BehaviorSource behaviorSource)
    {
        fileWriter.Write(string.Format("{0} = {1}.New()", className, "BehaviorTreeRoot")+ line_end);
        fileWriter.Write(line_end);

        fileWriter.Write(string.Format("function {0}.New()", className) + line_end);
        fileWriter.Write(line_end);
        fileWriter.Write(string.Format("\tlocal root = {{}}")+ line_end);
        fileWriter.Write(string.Format("\tsetmetatable(root,  {{__index = {0}}})", className) + line_end);
        fileWriter.Write(string.Format("\troot.__index = root") + line_end);
        fileWriter.Write(string.Format("\troot.name = \"{0}\"", className) + line_end);

        int nodeIdx = 0;
        fileWriter.Write(string.Format("\tdo") + line_end);
        ExportToLua.ExportNode(fileWriter, "root", behaviorSource.RootTask, 2, ref nodeIdx);
        fileWriter.Write(string.Format("\tend") + line_end);

        fileWriter.Write(line_end);
        fileWriter.Write(string.Format("\treturn root") + line_end);
        fileWriter.Write(string.Format("end") + line_end);

        fileWriter.Write(line_end);
        fileWriter.Write(string.Format("return {0}.New()", className) + line_end);
    }

    private static void ExportNode(StreamWriter fileWriter, string parentName, Task task, int indentDepth, ref int nodeIdx)
    {
        string nodeName = string.Format("node{0}", ++nodeIdx);
        string indent = string.Empty;
        for(int i = 0; i < indentDepth; ++i)
        {
            indent += "\t";
        }

        fileWriter.Write(string.Format("{0}local {1} = {2}.New()", indent, nodeName, task.FriendlyName) + line_end);
        fileWriter.Write(string.Format("{0}{1}:AddChild({2})", indent, parentName, nodeName) + line_end);


        if(task is ParentTask)
        {
            ParentTask parentTask = task as ParentTask;
            if(parentTask.Children != null && parentTask.Children.Count > 0)
            {
                fileWriter.Write(string.Format("{0}do", indent) + line_end);

                int childIndentDepth = indentDepth + 1;
                for(int i = 0; i < parentTask.Children.Count; i++)
                {
                    ExportToLua.ExportNode(fileWriter, nodeName, parentTask.Children[i], childIndentDepth, ref nodeIdx);
                }

                fileWriter.Write(string.Format("{0}end", indent) + line_end);
            }
        }

    }

}
