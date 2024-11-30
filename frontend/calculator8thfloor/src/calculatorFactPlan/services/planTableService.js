class PlanTableService {
    constructor() {
      this.isPlanTable = false;
    }
  
    setPlanTable(isPlanTable) {
      this.isPlanTable = isPlanTable;
      localStorage.setItem('isPlanTable', isPlanTable.toString());
    }
  
    getPlanTable() {
      const isPlanTableString = localStorage.getItem('isPlanTable');
      return isPlanTableString === 'true';
    }
  
    clearPlanTableStatus() {
      this.isPlanTable = false;
      localStorage.removeItem('isPlanTable');
    }
  }
  
  export default new PlanTableService();