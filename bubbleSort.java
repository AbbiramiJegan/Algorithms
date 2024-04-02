public class BubbleSort {
    public static void bubbleSort(int[] A) {
        int n = A.length;
        // Perform n - 1 passes
        for (int i = 0; i < n - 1; i++) {
            // In each pass, one element is compared with the next element
            for (int j = 0; j < n - i - 1; j++) {
                if (A[j] > A[j + 1]) {
                    // Swap the elements
                    int temp = A[j];
                    A[j] = A[j + 1];
                    A[j + 1] = temp;
                }
            }
        }
    }

    public static void main(String[] args) {
        int[] arr = {64, 34, 25, 12, 22, 11, 90};
        bubbleSort(arr);
        System.out.print("Sorted array: ");
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }
    }
}
