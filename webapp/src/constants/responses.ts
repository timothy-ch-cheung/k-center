interface algorithm_props {
    message: string
    additionalInfo: string
}

export const responses: { [key: string]: algorithm_props } = {
    none: {
        message: "",
        additionalInfo: ""
    },
    brute_force_k_center_predicted_time: {
        message: "how was this calculated?",
        additionalInfo: `The number of candidates, from the set of points length n, with k centers is n choose k (ⁿCₖ). 
        The time to check a small number of candidates is recorded and an average is taken to find the time to check a 
        typical candidate (Τ). Therefore the worst case estimated time is ⁿCₖ × Τ.`
    },
    brute_force_colourful_k_center_predicted_time: {
        message: "how was this calculated?",
        additionalInfo: `The number of candidates, from the set of points length n, with k centers is n choose k (ⁿCₖ). 
        There are also n² different weights that need to be tested for each candidate. The time to check a small number 
        of candidates is recorded and an average is taken to find the time to check a typical candidate (Τ). Therefore 
        the worst case the estimated time is n² × ⁿCₖ × Τ.`
    }
}