import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static class Node {
        Map<String, Node> childNode = new HashMap<>();
        Node() {}
        public void insert(String str) {
            Node node = this;
            String[] S = str.split("\\\\");
            for (String s : S) {
                node.childNode.putIfAbsent(s, new Node());
                node = node.childNode.get(s);
            }
        }

        public void print(Node now, int d) {
            Node node = now;
            if (node.childNode != null) {
                List<String> list = new ArrayList<>(node.childNode.keySet());
                Collections.sort(list);
                for (String str : list) {
                    for (int i = 0; i < d; i++) {
                        System.out.print(" ");
                    }
                    System.out.println(str);
                    print(node.childNode.get(str), d + 1);
                }
            }
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        Node trie = new Node();
        for (int i = 0; i < n; i++) {
            String line = br.readLine();
            trie.insert(line);
        }
        trie.print(trie, 0);
    }
}