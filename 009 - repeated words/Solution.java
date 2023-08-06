import java.util.Arrays;
import java.util.List;
import java.util.Objects;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Solution {

    private static String regex = "\\b(\\w+)\\b(\\s+\\b\\1\\b)+";
    private static Pattern pattern = Pattern.compile(regex, Pattern.CASE_INSENSITIVE);

    private static String resolve(String incase) {
        Matcher matcher = pattern.matcher(incase);
        while (matcher.find()) {
            String g = matcher.group();
            String g1 = matcher.group(1);
            incase = incase.replaceAll(g, g1);
        }
        return incase;
    }

    public static void main(String[] args) {
        List<Test> tests = Arrays.asList(
                new Test(
                        "Goodbye bye bye world world world",
                        "Goodbye bye world"),
                new Test(
                        "Sam went went to to to his business",
                        "Sam went to his business"),
                new Test(
                        "Reya is is the the best player in eye eye game",
                        "Reya is the best player in eye game"),
                new Test(
                        "in inthe",
                        "in inthe"),
                new Test(
                        "Hello hello Ab aB",
                        "Hello Ab"),
                new Test(
                        "tap taptap For fOr for forfor",
                        "tap taptap For forfor"),
                new Test(
                        "taptap of kirethe the hte hTe hte",
                        "taptap of kirethe the hte"),
                new Test(
                        "tim tamtim tam tam ta tam tam",
                        "tim tamtim tam ta tam"),
                new Test(
                        "a a a a a a a a a a a a a a a a",
                        "a"),
                new Test(
                        "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"));
        for (int i = 0; i < tests.size(); i++) {
            Test test = tests.get(i);
            String incase = test.incase;
            String expect = test.expect;
            String result = resolve(incase);
            if (Objects.equals(expect, result)) {
                System.out.println("Test " + i + " success!");
            } else {
                System.out.println("Test " + i + " fail!!!");
                System.out.println("InCase:");
                System.out.println(incase);
                System.out.println("Expect:");
                System.out.println(expect);
                System.out.println("Result:");
                System.out.println(result);
            }
        }
    }
}

class Test {
    String incase;
    String expect;

    Test(String incase, String expect) {
        this.incase = incase;
        this.expect = expect;
    }
}