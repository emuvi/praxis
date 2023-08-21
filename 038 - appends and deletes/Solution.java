import java.util.Objects;

public class Solution {

    public static String appendAndDelete(String origin, String destiny, int steps) {
        int same_count = 0;
        for (int i = 0; i < Math.min(origin.length(), destiny.length()); i++) {
            if (Objects.equals(origin.charAt(i), destiny.charAt(i))) {
                same_count++;
            } else {
                break;
            }
        }
        var remaining_to_delete = origin.length() - same_count;
        var remaining_to_append = destiny.length() - same_count;
        var total_count = remaining_to_delete + remaining_to_append;
        return steps - total_count >= 0
                && (steps - total_count) % 2 == 0
                || steps >= origin.length() + destiny.length()
                        ? "Yes"
                        : "No";
    }

    public static void main(String[] args) {
        var tests = new Test[] {
                new Test("abcd", "abcdert", 10, "No")
        };
        for (int i = 0; i < tests.length; i++) {
            var test = tests[i];
            var result = appendAndDelete(test.origin, test.destiny, test.steps);
            if (Objects.equals(test.expects, result)) {
                System.out.println(String.format("Test %d success!", i));
            } else {
                System.out.println(String.format("Test %d fails!!!", i));
                System.out.println("Expected:");
                System.out.println(test.expects);
                System.out.println("Resulted:");
                System.out.println(result);
            }
        }
    }

    static class Test {

        String origin;
        String destiny;
        int steps;
        String expects;

        public Test(String origin, String destiny, int steps, String expects) {
            this.origin = origin;
            this.destiny = destiny;
            this.steps = steps;
            this.expects = expects;
        }

    }

}